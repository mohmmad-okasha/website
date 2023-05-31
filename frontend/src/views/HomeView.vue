<template>
  <div class="home">
    <!-- ======= Header ======= -->
    <header id="header" class="header d-flex align-items-center">
      <div class="container-fluid container-xl d-flex align-items-center justify-content-between">

        <a href="index.html" class="logo d-flex align-items-center">
          <!-- Uncomment the line below if you also wish to use an image logo -->
          <!-- <img src="assets/img/logo.png" alt=""> -->
          <h1><span>.</span> جامعة فلسطين التقنية</h1>
        </a>

        <i class="mobile-nav-toggle mobile-nav-show bi bi-list"></i>
        <i class="mobile-nav-toggle mobile-nav-hide d-none bi bi-x"></i>
        <nav id="navbar" class="navbar">
          <ul>
            <li><a href="index.html" class="active">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="projects.html">Projects</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li class="dropdown"><a href="#"><span>Dropdown</span> <i
                  class="bi bi-chevron-down dropdown-indicator"></i></a>
              <ul>
                <li><a href="#">Dropdown 1</a></li>
                <li class="dropdown"><a href="#"><span>Deep Dropdown</span> <i
                      class="bi bi-chevron-down dropdown-indicator"></i></a>
                  <ul>
                    <li><a href="#">Deep Dropdown 1</a></li>
                    <li><a href="#">Deep Dropdown 2</a></li>
                    <li><a href="#">Deep Dropdown 3</a></li>
                    <li><a href="#">Deep Dropdown 4</a></li>
                    <li><a href="#">Deep Dropdown 5</a></li>
                  </ul>
                </li>
                <li><a href="#">Dropdown 2</a></li>
                <li><a href="#">Dropdown 3</a></li>
                <li><a href="#">Dropdown 4</a></li>
              </ul>
            </li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </nav><!-- .navbar -->

      </div>
    </header><!-- End Header -->

    <!-- ======= Hero Section ======= -->
    <section id="hero" class="hero">

      <div class="info d-flex align-items-center">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-lg-6 text-center">
              <h2 data-aos="fade-down"> <span>كلية الهندسة والتكنولوجي</span></h2>
              <p data-aos="fade-up">التميّز والرّيادة في مجالي التّعليم الهندسي والبحث العلمي على المستويين المحلّي
                والدُولي</p>
              <a data-aos="fade-up" data-aos-delay="200" @click="go_to()" class="btn-get-started"><i
                  class="fa fa-arrow-down"></i></a>
            </div>
          </div>
        </div>
      </div>

      <div id="hero-carousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
        <div class="carousel-item active" style="background-image: url(static/assets/img/main.png)"></div>
      </div>

    </section><!-- End Hero Section -->

    <!-- ======= Subjects Section ======= -->
    <section id="services" class="services section-bg">
      <div class="container" data-aos="fade-up">

        <div class="section-header">
          <h2>المواد</h2>
        </div>
        <div class="row gy-4 rtl">
          <div v-for="s in subjects" :key="s.id" class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">

            <router-link tag="div" :to="'/subject/' + s.name" class="service-item  position-relative">


              <h3>{{ s.name }}</h3>
              <p>{{ s.description.substr(0, 40) + '..' }}</p>
              <a class="readmore stretched-link"></a>
              <div class="post-img position-relative overflow-hidden">
                <img :src="'media/subjects/' + s.id + '_' + s.name + '.jpg'" class="image-container img-fluid" alt="">
              </div>
            </router-link>
          </div><!-- End Service Item -->
        </div>

      </div>
    </section><!-- End Subjects Section -->



  </div>
</template>
<script>
/* eslint-disable */
// @ is an alias to /src
import axios from 'axios';
import { my_api, domain_url } from "../axios-api";
import NavBar from '../components/parts/NavBar.vue'
export default {
  name: "HomeView",
  components: {
    NavBar,
  },
  data() {
    return {
      subjects: [],
    }
  },
  computed: {
    search() {
      let data = this.$parent.$refs.NavBar.search
      if (data && data.trim()) { // data.trim() to check data not spaces only
        return axios({
          method: "get",
          url: domain_url + "/backend/subjects/?search=" + data,
        }).then((response) => (this.subjects = response.data));
      } else {
        this.get_subjects();
      }
    },
  },
  async mounted() {
    await this.get_subjects();
  },
  methods: {
    get_subjects() {
      return my_api.get('/backend/subjects/')
        .then((response) => (this.subjects = response.data))
        .catch(err => { alert(err) });
    }
  }
};
</script>
