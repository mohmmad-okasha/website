<template>
  <div class="home">
    <!-- ======= Header ======= -->
    <header id="header" class="header d-flex align-items-center">
      <div class="container-fluid container-xl d-flex align-items-center justify-content-between">

        <a href="#" class="logo d-flex align-items-center">
          <!-- Uncomment the line below if you also wish to use an image logo -->
          <!-- <img src="assets/img/logo.png" alt=""> -->
          <h1>.<span>(خضوري)</span> جامعة فلسطين التقنية</h1>
        </a>



      </div>
    </header><!-- End Header -->

    <!-- ======= Hero Section ======= -->
    <section id="hero" class="hero">

      <div class="info d-flex align-items-center">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-lg-6 text-center">
              <h2 data-aos="fade-down"> <span>نادي هندسة البناء</span></h2>
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

          <div class="form-floating mb-5 rtl">
            <input type="text" class="form-control" v-model="search" placeholder="name@example.com">
            <label for="floatingInput">بحث</label>
          </div>
        </div>

        <div class="row gy-4 rtl">
          <div v-for="s in subjects" :key="s.id" class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">

            <router-link tag="div" :to="'/subject/' + s.name" class="service-item  position-relative">


              <h3>{{ s.name }}</h3>
              <p v-if="s.description">{{ s.description.substr(0, 40) + '..' }}</p>
              <a class="readmore stretched-link"></a>
              <div class="post-img position-relative overflow-hidden">
                <img v-if="imageExists(s)" :src="'media/subjects/' + s.id + '_' + s.name + '.jpg'" class="image-container img-fluid" alt="">
              </div>
            </router-link>
          </div><!-- End Service Item -->
        </div>

      </div>
    </section><!-- End Subjects Section -->

    <!-- ======= Footer ======= -->
    <footer id="footer" class="footer">

      <div class="footer-content position-relative">
        <div class="container">
          <div class="row">

            <div class="col-lg-4 col-md-6">
              <div class="footer-info">
                <h3>نادي هندسة البناء</h3>
                <!-- <p>
                  <br>
                  <strong>Phone:</strong> +1 5589 55488 55<br>
                  <strong>Email:</strong> info@example.com<br>
                </p> -->
                <div class="social-links d-flex mt-3">
                  <a target="_blank" href="https://www.facebook.com/profile.php?id=100063528045057&mibextid=ZbWKwL"
                    class="d-flex align-items-center justify-content-center"><i class="bi bi-facebook"></i></a>
                  <a target="_blank"
                    href="https://l.facebook.com/l.php?u=https%3A%2F%2Ft.me%2Fbeclub2022%3Ffbclid%3DIwAR2UKCFRoRjpzgtaRDpVmvHyFA2s-Eaf6uDPH8UQk_S-oVMTZKWbg787-bg&h=AT23yxNiq63dtJmxysxI9y3sXiPW7zrg7DLuCUgjAM34m88b8L68x6KdnqMRrMmHRlK2YJHXP4agwkoGmVrTOrkloTuVVXR58ayUkBALsfCjU6try-TzipS4_jf749HHb3pYFA"
                    class="d-flex align-items-center justify-content-center"><i class="bi bi-telegram"></i></a>
                  <a target="_blank"
                    href="https://l.facebook.com/l.php?u=https%3A%2F%2Fyoutube.com%2F%40ABDELFATTAHSAMARA%3Ffbclid%3DIwAR34NJNafV0bFHITBI62lIX7awYkYiW1sn5zanyoniNr-CTOqyAYHI2SX_I&h=AT1TpCNe1vycJvSgZoT4a0H8H5K-SJV8C_H2Jk69YPZ0DLqnrGvxa6wNpg81S8UNhchBxXDWkbqLE5qFhOwMt1oGGJrGcXtA9L18XLUHsk_EJGBUlvNmmcAm7_qx4KU6SMM7IzXMVYn14-o"
                    class="d-flex align-items-center justify-content-center"><i class="bi bi-youtube"></i></a>
                  <router-link tag="a" to="dashboard" class="d-flex align-items-center justify-content-center"><i
                      class="bi bi-book"></i></router-link>
                  <router-link tag="a" to="links" class="d-flex align-items-center justify-content-center"><i
                      class="bi bi-link"></i></router-link>
                </div>
              </div>

            </div><!-- End footer info column-->

          </div>
        </div>
      </div>

      <div class="footer-legal text-center position-relative">
        <div class="container">

        </div>
      </div>

    </footer>
    <!-- End Footer -->

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
  watch: {
    search(newValue) {
      if (newValue && newValue.trim()) { // data.trim() to check data not spaces only
        return axios({
          method: "get",
          url: domain_url + "/backend/subjects/?search=" + newValue,
        }).then((response) => (this.subjects = response.data));
      } else {
        this.get_subjects();
      }
    }

  },
  data() {
    return {
      subjects: [],
      search: '',
    }
  },

  async mounted() {
    await this.get_subjects();
  },
  methods: {
    get_subjects() {
      return my_api.get('/backend/subjects/')
        .then((response) => (this.subjects = response.data))
        .catch(err => { alert(err) });
    },
    go_to() {
      const myDiv = document.getElementById('services'); // Replace 'myDiv' with the ID of your target div
      myDiv.scrollIntoView({ behavior: 'smooth' });
    },
    imageExists(subject) {
      const imgPath = `media/subjects/${subject.id}_${subject.name}.jpg`;
      const img = new Image();
      img.src = imgPath;
      return img.complete && img.naturalWidth !== 0;
    },
  }
};
</script>
