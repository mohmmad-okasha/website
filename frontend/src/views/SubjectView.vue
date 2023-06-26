<template>
    <div>

        <section id="services" class="services section-bg">
            <div class="container" data-aos="fade-up">

                <div class="section-header">
                    <h2>{{ $route.params.subject_name }} </h2>
                    <div class="post-img position-relative overflow-hidden">
                        <img  v-if="imageExists()" :src="'media/subjects/' + this.subject_id + '_' + $route.params.subject_name + '.jpg'"
                            class="image-container img-fluid" alt="">
                    </div>
                    <br>
                    <a href="#" @click="$router.go(-1)"><i class="fa-solid fa-house"></i></a>

                </div>


                <section id="blog" class="blog rtl">

                    <div class="form-floating mb-5 rtl">
                        <input type="text" class="form-control" v-model="search" placeholder="name@example.com">
                        <label for="floatingInput">بحث</label>
                    </div>

                    <div class="container" data-aos="fade-up" data-aos-delay="200">
                        <div class="row gy-4 posts-list">
                            <div v-for="l in links" :key="l.id" class="col-xl-4 col-md-6">
                                <div class="post-item position-relative h-100">
                                    <div class="post-img position-relative overflow-hidden">
                                        <img src="static/assets/img/main.jpg" class="img-fluid" alt="">
                                        <span class="post-date">{{ l.timestamp }}</span>
                                    </div>
                                    <div class="post-content d-flex flex-column">
                                        <h3 class="post-title">{{ l.title }}</h3>
                                        <p>{{ l.description }}</p>
                                        <hr>
                                        <a :href="'https://' + l.url" target="_blank"
                                            class="readmore stretched-link"><span>Open</span><i
                                                class="bi bi-arrow-right"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

            </div>
        </section>



    </div>
</template>
<script>
/* eslint-disable */
// @ is an alias to /src
import axios from 'axios';
import { my_api, domain_url } from "../axios-api";
import NavBar from '../components/parts/NavBar.vue'
export default {
    name: "SubjectView",
    components: {
        NavBar,
    },
    data() {
        return {
            search: '',
            subject: '',
            subject_id: '',
            links: [],
        }
    },
    watch: {
        search(newValue) {
            if (newValue && newValue.trim()) { // data.trim() to check data not spaces only
                return axios({
                    method: "get",
                    url: domain_url + "/backend/links/?search=" + newValue + "&subject_id=" + this.subject_id,
                }).then((response) => (this.links = response.data));
            } else {
                this.get_links();
            }
        }

    },

    async mounted() {
        await this.get_subject_id();
        await this.get_links();
        window.scrollTo(0, 0); // scroll to top on load

    },
    methods: {
        imageExists() {
            const imageUrl = 'media/subjects/' + this.subject_id + '_' + this.$route.params.subject_name + '.jpg';
            const http = new XMLHttpRequest();

            http.open('HEAD', imageUrl, false);
            http.send();

            return http.status !== 404;
        },
        get_subject_id() {
            return axios({
                method: "get",
                url: domain_url + "/backend/get_subject_id/?subject=" + this.$route.params.subject_name,
                //auth: { username: "admin", password: "123", },
            }).then((response) => (this.subject_id = response.data.subject_id));
        },
        get_links() {
            return axios({
                method: "get",
                url: domain_url + "/backend/get_links/?subject=" + this.subject_id,
                //auth: { username: "admin", password: "123", },
            }).then((response) => (this.links = response.data));
        }
    }
};
</script>