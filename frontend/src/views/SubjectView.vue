<template>
    <div>
        <div class="SubjectView" id="page-top">
            <router-link tag="button" :to="'/'" class="btn-close" aria-label="Close"></router-link>
        </div>
        <div class="container">
            <h2>{{ $route.params.subject_name }} Links </h2>
            <br>
            <section id="blog" class="blog rtl">
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
                                    <!-- <div class="meta d-flex align-items-center">
                                        <div class="d-flex align-items-center">
                                            <i class="bi bi-person"></i> <span class="ps-2">John Doe</span>
                                        </div>
                                        <span class="px-3 text-black-50">/</span>
                                        <div class="d-flex align-items-center">
                                            <i class="bi bi-folder2"></i> <span class="ps-2">Politics</span>
                                        </div>
                                    </div> -->
                                    <p>{{ l.description }}</p>
                                    <hr>
                                    <a :href="'https://' + l.url" target="_blank" class="readmore stretched-link"><span>Read More</span><i
                                            class="bi bi-arrow-right"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
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
            subject: '',
            subject_id: '',
            links: [],
        }
    },
    computed: {
        search() {
            let data = this.$parent.$refs.NavBar.search
            if (data && data.trim()) { // data.trim() to check data not spaces only
                return axios({
                    method: "get",
                    url: domain_url + "/backend/links/?search=" + data,
                }).then((response) => (this.links = response.data));
            } else {
                this.get_links();
            }
        },
    },
    async mounted() {
        await this.get_subject_id();
        await this.get_links();
    },
    methods: {
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