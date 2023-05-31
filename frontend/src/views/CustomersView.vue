<template>
    <!-- &nbsp; -->
    <div class="CustomersView">

        <!-- context-menu -->
        <div id="context-menu" class="context-menu" :style="menuStyle">
            <ul >
                <li class="dropdown-item" @click="delete_customer(customer.id)">
                    <i class="fa fa-trash"></i>
                    {{ $t("Delete") }}
                </li>
                <li class="ltr dropdown-item" @click="open_edit_modal">
                    <i class="fa fa-pen-to-square"></i>
                    {{ $t("Edit") }}
                </li>
                <li class="dropdown-item">
                    <i class="fa fa-print"></i>
                    {{ $t("Print") }}
                </li>
            </ul>
        </div>


        <!-- Table Card -->
        <div class="col-xl-12 center">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">{{ $t("Customers Table") }} </h6>
                    <div class="dropdown no-arrow">

                        <div class="btn-group" role="group">
                            <button id="btnGroupVerticalDrop1" type="button" class="btn dropdown-toggle"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                                <i class="fa fa-bars on-hover"></i>
                            </button>
                            <div class="dropdown-menu" aria-labelledby="btnGroupVerticalDrop1" x-placement="bottom-start"
                                style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 37px, 0px);">
                                <a class="dropdown-item" @click="open_add_modal">
                                    <i class="fa fa-plus"></i>
                                    {{ $t("Add") }}
                                </a>
                                <a class="dropdown-item" @click="PrintDiv('table')">
                                    <i class="fa fa-print"></i>
                                    {{ $t("Print") }}
                                </a>
                            </div>
                        </div>

                    </div>
                </div>
                <!-- Card Body -->
                <div id="table" class="card-body">
                    <div class="card-header cnter" style="display: none;" id="head_txt"></div>
                    <form class="site-form-table">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">{{ $t("Name") }}</th>
                                    <th scope="col">{{ $t("Mobile") }}</th>
                                    <th scope="col">{{ $t("Type") }}</th>
                                    <th scope="col">{{ $t("ID Type") }}</th>
                                    <th scope="col">{{ $t("ID Number") }}</th>
                                    <th scope="col">{{ $t("Address") }}</th>
                                    <th scope="col">{{ $t("Notes") }}</th>
                                    <th scope="col" class="no_print">{{ $t("Image") }}</th>
                                    <th scope="col" class="no_print">{{ $t("Actions") }}</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr @contextmenu="showContextMenu" v-for="customer in this.customers" :key="customer.id"
                                    @click="row_click(customer.id)" @click.right="row_click(customer.id)" @dblclick="open_edit_modal" role="button"
                                    :class="{ 'selected': customer.id === active_index }">
                                    <th scope="row" id="id">{{ customer.id }}</th>
                                    <td>{{ $t(customer.name) }}</td>
                                    <td>{{ $t(customer.mobile) }}</td>
                                    <td>{{ $t(customer.type) }}</td>
                                    <td>{{ $t(customer.id_type) }}</td>
                                    <td>{{ $t(customer.id_number) }}</td>
                                    <td>{{ $t(customer.address) }}</td>
                                    <td>{{ $t(customer.notes) }}</td>
                                    <td class="no_print">
                                        <img :src="base_url + customer.id + '_' + customer.name + '.png'"
                                            @error="$event.target.src = base_url + 'profile.png'" alt="No Image" width="40"
                                            height="40" class="img-profile on-hover-l" />
                                    </td>
                                    <td class="no_print">

                                        <div class="btn-group" role="group">
                                            <button @click.right="alert('1')" id="btnGroupVerticalDrop1" type="button" class="btn dropdown-toggle"
                                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                                                <i class="fa fa-gear on-hover"></i>
                                            </button>
                                            <div  class="dropdown-menu" aria-labelledby="btnGroupVerticalDrop1"
                                                x-placement="bottom-start"
                                                style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 37px, 0px);">
                                                <a class="dropdown-item" @click="delete_customer(customer.id)">
                                                    <i class="fa fa-trash"></i>
                                                    {{ $t("Delete") }}
                                                </a>
                                                <a class="dropdown-item" @click="open_edit_modal">
                                                    <i class="fa fa-pen-to-square"></i>
                                                    {{ $t("Edit") }}
                                                </a>
                                                <a class="dropdown-item">
                                                    <i class="fa fa-print"></i>
                                                    {{ $t("Print") }}
                                                </a>
                                            </div>
                                        </div>

                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <!-- to get id of selected record -->
                        <input hidden type="text" v-model="active_index" id="row_id" />
                    </form>
                </div>
            </div>
        </div>

        <!-- to get search value from navbar -->
        <input :value="this.$parent.$refs.NavBar.search" v-bind:on-change="search" hidden>

        <!-- modal -->
        <div class="modal fade" id="addModal" data-backdrop="static" data-keyboard="false" tabindex="-1"
            aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 v-if="!this.edit_mode" class="modal-title" id="modal_label">{{ $t("Add Customer") }}</h5>
                        <h5 v-if="this.edit_mode" class="modal-title" id="modal_label">{{ $t("Edit Customer") }}</h5>
                        <button type="button" class="close on-hover" @click="this.closeModal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">

                        <form>
                            <div class="form-group">
                                <label for="customer_name">{{ $t("Name") }}</label>
                                <input id="customer_name" v-model="customer.name" type="text"
                                    :class="{ 'is-invalid': !this.customer.name && this.validate, 'is-valid': this.customer.name && this.validate }"
                                    class="form-control">
                                <div v-if="!this.customer.name && this.validate" class="invalid-feedback hidden">
                                    {{ $t("Please Enter The Name") }}
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-sm-4">
                                    <div class="form-group">
                                        <label for="cutomer_type">{{ $t("Type") }}</label>
                                        <select id="cutomer_type" v-model="customer.type" type="text" class="form-control"
                                            :class="{ 'is-invalid': !this.customer.type && this.validate, 'is-valid': this.customer.type && this.validate }">
                                            <option selected :value="$t('Customer')">{{ $t("Customer") }}</option>
                                            <option :value="$t('Supplier')">{{ $t("Supplier") }}</option>
                                        </select>
                                        <div v-if="!this.customer.type && this.validate" class="invalid-feedback hidden">
                                            {{ $t("Please Select Type") }}
                                        </div>
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="form-group mb-2">
                                        <label for="cutomer_mobile">{{ $t("Mobile") }}</label>
                                        <input id="cutomer_mobile" v-model="customer.mobile" type="text"
                                            :class="{ 'is-invalid': !this.customer.mobile && this.validate, 'is-valid': this.customer.mobile && this.validate }"
                                            class="form-control">
                                        <div v-if="!this.customer.type && this.validate" class="invalid-feedback hidden">
                                            {{ $t("Please Enter Mobile Number") }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-sm-4">
                                    <div class="form-group">
                                        <label for="id_type">{{ $t("ID Type") }}</label>
                                        <select id="id_type" v-model="customer.id_type" type="text" class="form-control"
                                            :class="{ 'is-invalid': !this.customer.id_type && this.validate, 'is-valid': this.customer.id_type && this.validate }">
                                            <option selected :value="$t('ID Card')"> {{ $t("ID Card") }}</option>
                                            <option :value="$t('Passport')"> {{ $t("Passport") }}</option>
                                            <option :value="$t('Driving License')"> {{ $t("Driving License") }}</option>
                                            <option :value="$t('Residence')"> {{ $t("Residence") }}</option>
                                        </select>
                                        <div v-if="!this.customer.id_type && this.validate" class="invalid-feedback hidden">
                                            {{ $t("Please Select ID Type") }}
                                        </div>
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="form-group mb-2">
                                        <label for="id_number">{{ $t("Number of") }} {{ customer.id_type }} </label>
                                        <input id="id_number" v-model="customer.id_number" type="text"
                                            :class="{ 'is-invalid': !this.customer.id_number && this.validate, 'is-valid': this.customer.id_number && this.validate }"
                                            class="form-control">
                                        <div v-if="!this.customer.id_number && this.validate"
                                            class="invalid-feedback hidden">
                                            {{ $t("Please Enter ID Number") }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group ">
                                <label for="cutomer_address"> {{ $t("Address") }}</label>
                                <input id="cutomer_address" v-model="customer.address"
                                    :class="{ 'is-invalid': !this.customer.address && this.validate, 'is-valid': this.customer.address && this.validate }"
                                    type="text" class="form-control">
                                <div v-if="!this.customer.address && this.validate" class="invalid-feedback hidden">
                                    {{ $t("Please Enter The Address") }}
                                </div>
                            </div>
                            <div class="form-group ">
                                <label for="cutomer_notes"> {{ $t("Notes") }}</label>
                                <textarea class="form-control" v-model="customer.notes" id="cutomer_notes"
                                    rows="1"></textarea>
                            </div>
                            <br>
                            <div class="form-group ">
                                <div class="container ">
                                    <div class="picture-container">
                                        <div class="picture">
                                            <img :src="previewImage || base_url + 'profile.png'" width="100" height="150"
                                                class="picture-src" id="wizardPicturePreview">
                                            <input v-on:change="onFileChange" type="file" id="wizard-picture" class="">
                                        </div>
                                        <br>
                                        <h6 class=""> {{ $t("Choose Picture") }}</h6>
                                    </div>
                                </div>
                            </div>
                        </form>

                    </div>
                    <div class="modal-footer">

                        <button type="button" id="closeModal" title="close" class="btn btn-secondary on-hover-sm"
                            @click="this.closeModal">
                            <i class="fa fa-xmark"></i>
                        </button>

                        <button v-if="!edit_mode" type="button" title="save" @click="save_customer()"
                            class="btn btn-primary on-hover-sm">
                            <i class="fa fa-floppy-disk"></i></button>

                        <button v-if="edit_mode" type="button" title="delete" @click="delete_customer(active_index)"
                            class="btn btn-danger on-hover-sm"> <i class="fa fa-trash"></i> </button>

                        <button v-if="edit_mode" type="button" title="save" @click="update_customer(active_index)"
                            class="btn btn-primary on-hover-sm"> <i class="fa fa-floppy-disk"></i> </button>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import { my_api, domain_url } from "../axios-api";
import { lang, change_lang } from '../main';

import NavBar from '../components/parts/NavBar.vue'

export default {
    name: 'CustomersView',
    components: {
        NavBar,
    },

    data() {
        return {
            validate: false, //for check forms
            base_url: window.location.origin + '/media/customers/',//for images 
            previewImage: null,// to show selected image before save
            img_file: null,
            active_index: null,//current id
            customers: [],
            customer: {
                name: "",
                mobile: "",
                type: "",
                id_type: "",
                id_number: "",
                address: "",
                notes: "",
                //img: "default.png",
            },
            edit_mode: false,
            max_id: 0,
            isContextMenuActive: false,
            menuStyle: {
                display: 'none',
                top: 0,
                left: 0
            }
        }
    },

    async mounted() {
        //to remove modal background on auto vue js reload
        const elements = document.getElementsByClassName("modal-backdrop fade show");
        while (elements.length > 0) {
            elements[0].parentNode.removeChild(elements[0]);
        }////

        await this.get_customers();

    },

    computed: {
        search() {
            let data = this.$parent.$refs.NavBar.search
            if (data && data.trim()) { // data.trim() to check data not spaces only
                return axios({
                    method: "get",
                    url: domain_url + "/backend/customers/?search=" + data,
                }).then((response) => (this.customers = response.data));
            } else {
                this.get_customers();
            }
        },
    },

    methods: {



        showContextMenu(event) {
            event.preventDefault();
            this.isContextMenuActive = true;
            this.menuStyle.top = `${event.clientY}px`;
            this.menuStyle.left = `${event.clientX}px`;
            this.menuStyle.display = 'block';
            // Add a click listener to the window object to hide the context menu
            window.addEventListener('click', this.hideContextMenu);
        },

        hideContextMenu() {
            this.isContextMenuActive = false;
            this.menuStyle.display = 'none';
            // Remove the click listener from the window object
            window.removeEventListener('click', this.hideContextMenu);
        },


        PrintDiv(id) {
            var divToPrint = document.getElementById(id);
            var popupWin = window.open('', '_blank', 'width=100000,height=10000');
            document.getElementById('head_txt').style.display = "block";
            document.getElementById('head_txt').innerHTML = this.$t("Customers");
            popupWin.document.write('<link href="static/css/sb-admin-2.min.css" rel="stylesheet">');
            popupWin.document.write('<link href="static/css/reports.css" rel="stylesheet">');
            popupWin.document.write('<style>body{background-color:white !important;}</style>');
            popupWin.document.write('<iframe src="static/parts/report_head.html" width="100%" height="200px" frameBorder="0"></iframe>');
            popupWin.document.write('<html><body onload="window.print()"> ' + divToPrint.innerHTML + '</html>');
            document.getElementById('head_txt').style.display = "none";
            popupWin.document.close();
        },

        onFileChange(e) {
            try {
                this.img_file = e.target.files[0];
                this.previewImage = URL.createObjectURL(this.img_file);
            } catch (err) {
                alert(err);
            }
        },

        uploadImage() {
            if (this.img_file) {
                let formData = new FormData()
                formData.append('image', this.img_file)
                return axios.post(domain_url + "/backend/upload_file/?file_name=/customers/" + this.max_id + '_' + this.customer.name + '.png', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                    .then(response => {
                        // handle successful response
                    })
                    .catch(error => {
                        alert(error)
                    })
            }
        },

        remove_file(file_name) {
            return axios({
                method: "get",
                url: domain_url + "/backend/remove_file/?file_name=" + file_name,
                auth: { username: "admin", password: "123" },
            });
        },

        get_customers() {
            // we using return first of the function for 'await' 
            return my_api.get('/backend/customers/')
                .then((response) => (this.customers = response.data))
                .catch(err => { alert(err) });
        },

        async save_customer() {
            try {
                if (this.check_form()) {
                    var response = await fetch(domain_url + "/backend/customers/", {
                        method: "post",
                        headers: { "Content-Type": "application/json", },
                        body: JSON.stringify(this.customer),
                    });

                    swal(this.$t("Added!"), { buttons: false, icon: "success", timer: 2000, });
                    this.get_customers();
                    await this.get_max_id();
                    await this.uploadImage();
                    this.closeModal();
                }
            } catch (error) { console.error(); }
        },

        async update_customer(id) {
            try {
                if (this.check_form()) {
                    var response = await fetch(domain_url + "/backend/customers/" + id + "/", {
                        method: "PUT",
                        headers: { "Content-Type": "application/json", },
                        body: JSON.stringify(this.customer),
                    }
                    );
                    swal(this.$t("Updated!"), { buttons: false, icon: "success", timer: 2000, });
                    this.max_id = this.customer.id
                    await this.uploadImage();
                    this.get_customers();
                    this.closeModal();
                    this.edit_mode = false;
                }
            } catch (error) {
                console.error();
            }

        },

        async delete_customer(id) {
            try {
                await swal({ title: this.$t("Are you sure to delete?"), text: "", icon: "warning", buttons: true, dangerMode: true, })
                    .then(async (willDelete) => {
                        if (willDelete) {
                            await my_api.delete('/backend/customers/' + id + '/')
                            this.remove_file('/customers/' + id + '_' + this.customer.name + '.png')
                            swal(this.$t("Deleted!"), { buttons: false, icon: "success", timer: 2000, });
                            await this.get_customers(); this.closeModal();
                        }
                    });
            } catch (error) { console.error(); }
        },

        async get_customer(id) {
            return axios({
                method: "get",
                url: domain_url + "/backend/customers/?id=" + id,
                auth: { username: "admin", password: "123", },
            }).then((response) => (this.customer = response.data[0]));
        },

        get_max_id() {
            return axios({
                method: "get",
                url: domain_url + "/backend/get_max_id/?table_name=Customers",
                //auth: { username: "admin", password: "123", },
            }).then((response) => (this.max_id = response.data.data.id__max));
        },

        open_add_modal() {
            this.edit_mode = false;
            //$('#modal_label').html('Add Customer');
            this.clear_form();
            $('#addModal').modal('toggle');
        },

        open_edit_modal() {
            this.edit_mode = true;
            //$('#modal_label').html('Edit Customer');
            $('#addModal').modal('toggle');
        },

        closeModal() {
            $('#addModal').modal('hide');
            this.clear_form();
        },

        async row_click(index) {
            this.active_index = index; //to change row color
            await this.get_customer(index);
            this.previewImage = this.base_url + this.customer.id + '_' + this.customer.name + '.png';
        },

        clear_form() {
            this.customer.name = '';
            this.customer.address = '';
            this.customer.mobile = '';
            this.customer.type = '';
            this.customer.id_number = '';
            this.customer.id_type = '';
            this.customer.notes = '';
            this.img_file = null;
            this.previewImage = null;
            this.validate = false;
        },

        check_form() {
            this.validate = true; //to change inputs color 'red/green'

            if (this.customer.name && this.customer.address && this.customer.mobile && this.customer.type && this.customer.id_type && this.customer.id_number) {
                return true
            } else {
                return false
            }
        },

    },
}

</script>
