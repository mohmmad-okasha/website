<template>
    <div class="SubjectsView">

        <div class="breadcrumbs d-flex align-items-center" style="background-image: url('assets/img/breadcrumbs-bg.jpg');">
            <div class="container position-relative d-flex flex-column align-items-center aos-init aos-animate"
                data-aos="fade">
                <h2>Dashboard</h2>
            </div>
        </div>


        
        <!-- ======= Subjects Section ======= -->
        <section id="services" class="services section-bg">
            <div class="container" data-aos="fade-up">

                <!-- subjects table -->
                <div class="col-xl-12 center">

                    <div class="card">

                        <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                            <h4>{{ $t("Subjects Table") }} </h4>
                            <div class="dropdown no-arrow">
                                <div class="form-group">
                                    <button v-if="!edit_mode" type="button" title="New" @click="open_add_modal()"
                                        class="btn btn-sm btn-outline-dark m-2 on-hover-sm">
                                        <i class="fa fa-plus"></i></button>
                                </div>
                            </div>
                        </div>

                        <div class="card-body">
                            <table class="table table-hover">
                                <thead>
                                    <tr>
                                        <th scope="col">#</th>
                                        <th scope="col">{{ $t("Subject") }}</th>
                                        <th scope="col">{{ $t("Description") }}</th>
                                        <th scope="col" class="no_print">{{ $t("Image") }}</th>
                                        <th scope="col" class="no_print">{{ $t("Actions") }}</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="s in this.subjects" :key="s.id" @click="row_click(s.id)"
                                        @click.right="row_click(s.id)" @dblclick="open_edit_modal">
                                        <th scope="row">{{ s.id }}</th>
                                        <td>{{ s.name }}</td>
                                        <td>{{ s.description.substr(0, 50) + '..' }}</td>
                                        <td class="no_print">
                                            <img :src="base_url + s.id + '_' + s.name + '.jpg'"
                                                @error="$event.target.src = base_url + 'base.jpg'" alt="No Image" width="40"
                                                height="40" class="img-profile on-hover-l" />
                                        </td>
                                        <td class="no_print">
                                            <button @click="delete_subject(s.id)" type="button"
                                                class="btn btn-sm btn-outline-dark m-2"><i class="fa fa-trash"></i></button>
                                            <button @click="open_edit_modal()" type="button"
                                                class="btn btn-sm btn-outline-dark m-2"><i
                                                    class="fa fa-pen-to-square"></i></button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

            </div>
        </section><!-- End Subjects Section -->






        <!-- modal -->
        <div class="modal  fade" id="addModal" data-backdrop="static" data-keyboard="false" tabindex="-1"
            aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog ">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 v-if="!this.edit_mode" class="modal-title" id="modal_label">{{ $t("Add subject") }}</h5>
                        <h5 v-if="this.edit_mode" class="modal-title" id="modal_label">{{ $t("Edit subject") }}</h5>
                        <button type="button" class="close on-hover" @click="this.closeModal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="form-group ">
                                <div class="container ">
                                    <div class="picture-container">
                                        <div class="picture">
                                            <img :src="previewImage" width="100" height="150" class="picture-src"
                                                id="wizardPicturePreview">
                                            <input v-on:change="onFileChange" type="file" id="wizard-picture" class="">
                                        </div>
                                        <br>
                                        <h6 class=""> {{ $t("Subject Picture") }}</h6>
                                    </div>
                                </div>
                            </div>

                            <div class="form-group">
                                <label for="name"> {{ $t("Subject name") }}</label>
                                <input id="name" v-model="subject.name"
                                    :class="{ 'is-invalid': !this.subject.name && this.validate, 'is-valid': this.subject.name && this.validate }"
                                    type="text" class="form-control">
                                <div v-if="!this.subject.name && this.validate" class="invalid-feedback hidden">
                                    {{ $t("Please Enter Name") }}
                                </div>
                            </div>
                            <br>
                            <div class="form-group ">
                                <label for="description"> {{ $t("description") }}</label>
                                <input id="description" v-model="subject.description" type="text" class="form-control">
                            </div>
                            <br>


                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" id="closeModal" title="close" class="btn btn-secondary on-hover-sm"
                            @click="this.closeModal">
                            <i class="fa fa-xmark"></i>
                        </button>
                        <button v-if="!edit_mode" type="button" title="save" @click="save_subject()"
                            class="btn btn-primary on-hover-sm">
                            <i class="fa fa-floppy-disk"></i></button>
                        <button v-if="edit_mode" type="button" title="delete" @click="delete_subject(active_index)"
                            class="btn btn-danger on-hover-sm"> <i class="fa fa-trash"></i> </button>
                        <button v-if="edit_mode" type="button" title="save" @click="update_subject(active_index)"
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
import NavBar from '../components/parts/NavBar.vue'
export default {
    name: "dashboard",
    components: {
        NavBar,
    },
    data() {
        return {
            base_url: window.location.origin + '/media/subjects/',//for images 
            previewImage: null,// to show selected image before save
            img_file: null,

            max_id: '',
            active_index: null,
            validate: false,
            saving: false,
            edit_mode: false,
            subjects: [],
            links: [],
            subject: {
                id: '',
                name: '',
                description: ''
            }
        }
    },
    computed: {
        search() {
            let data = this.$parent.$refs.NavBar.search
            if (data && data.trim()) { // data.trim() to check data not spaces only
                return axios({
                    method: "get",
                    url: domain_url + "/backend/dashboard_buttons/?search=" + data,
                }).then((response) => (this.buttons = response.data));
            } else {
                this.get_dashboard_buttons();
            }
        },
    },
    async mounted() {

        await this.get_subjects();
    },
    methods: {
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
                return axios.post(domain_url + "/backend/upload_file/?file_name=/subjects/" + this.max_id + '_' + this.subject.name + '.jpg', formData, {
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

        get_subjects() {
            return my_api.get('/backend/subjects/')
                .then((response) => (this.subjects = response.data))
                .catch(err => { alert(err) });
        },

        async save_subject() {
            try {
                if (this.check_form()) {
                    this.saving = true;
                    this.subject.timestamp = new Date().toLocaleString();
                    // save subject info
                    var response = await fetch(domain_url + "/backend/subjects/", {
                        method: "post",
                        headers: { "Content-Type": "application/json", },
                        body: JSON.stringify(this.subject),
                    });

                    if (!response.ok) {
                        // handle the error
                        var errorMessage = "Error: " + response.status + " " + response.statusText;
                        swal(errorMessage, { icon: 'error' });
                    } else {
                        // Request was successful

                        swal(this.$t("Added!"), { buttons: false, icon: "success", timer: 2000, });
                        this.get_subjects();
                        await this.get_max_id();
                        await this.uploadImage();

                        this.closeModal();
                    }
                    this.saving = false;

                }
            } catch (error) { console.error(); }
        },

        async delete_subject(id) {
            try {
                await swal({ title: this.$t("Are you sure to delete?"), text: "", icon: "warning", buttons: true, dangerMode: true, })
                    .then(async (willDelete) => {
                        if (willDelete) {
                            var response = await fetch(domain_url + '/backend/subjects/' + id + '/', {
                                method: "delete",
                                headers: { "Content-Type": "application/json", },
                            });
                            if (!response.ok) {
                                // handle the error
                                var errorMessage = "Error: " + response.status + " " + response.statusText;
                                swal(errorMessage, { icon: 'error' });
                            } else {
                                // Request was successful
                                swal(this.$t("Deleted!"), { buttons: false, icon: "success", timer: 2000, });
                                await this.get_subjects(); this.closeModal();
                            }
                        }
                    });
            } catch (error) { console.error(); }
        },

        async update_subject(id) {
            try {
                if (this.check_form()) {

                    var response = await fetch(domain_url + "/backend/subjects/" + id + "/", {
                        method: "PUT",
                        headers: { "Content-Type": "application/json", },
                        body: JSON.stringify(this.subject),
                    });

                    if (!response.ok) {
                        // handle the error
                        var errorMessage = "Error: " + response.status + " " + response.statusText;
                        swal(errorMessage, { icon: 'error' });
                    } else {
                        // Request was successful

                        swal(this.$t("Updated!"), { buttons: false, icon: "success", timer: 2000, });
                        this.max_id = this.subject.id
                        await this.uploadImage();

                        this.get_subjects();
                        this.closeModal();
                        this.edit_mode = false;
                    }
                }
            } catch (error) {
                console.error();
            }

        },
        open_add_modal() {
            this.edit_mode = false;
            this.clear_form();
            $('#addModal').modal('toggle');


        },

        open_edit_modal() {
            this.edit_mode = true;

            $('#addModal').modal('toggle');
            //to remove modal background on auto vue js reload
            const elements = document.getElementsByClassName("modal-backdrop fade show");
            while (elements.length > 0) {
                elements[0].parentNode.removeChild(elements[0]);
            }////
        },

        closeModal() {
            $('#addModal').modal('hide');
            this.clear_form();
        },

        clear_form() {
            this.subject.name = '';
            this.subject.description = '';
            this.img_file = null;
            this.previewImage = null;
            this.validate = false;
        },

        get_max_id() {
            return axios({
                method: "get",
                url: domain_url + "/backend/get_max_id/?table_name=Subjects",
                //auth: { username: "admin", password: "123", },
            }).then((response) => (this.max_id = response.data.data.id__max));
        },

        check_form() {
            this.validate = true; //to change inputs color 'red/green'

            if (
                this.subject.name
            ) {
                return true
            } else {
                return false
            }
        },

        async row_click(index) {
            this.active_index = index; //to change row color
            await this.get_subject(index);

            //this.previewImage = this.base_url + this.subject.id + '_' + this.subject.name + '.jpg';
        },

        async get_subject(id) {
            return axios({
                method: "get",
                url: domain_url + "/backend/subjects/?id=" + id,
                auth: { username: "admin", password: "123", },
            }).then((response) => (this.subject = response.data[0]));
        },


    },
}
</script>
