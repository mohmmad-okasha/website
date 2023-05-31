<template>
  <!-- <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/users">users</router-link>
    </nav>
    <router-view />
  </div> -->

  <div class="home" id="page-top"
    :style="{ '--primary': primary_color, '--back_color': back_color, '--primary_text': primary_text }">

    <!-- Login page -->
    <!-- <div v-if="!this.auth.logged_in">

      <section class="vh-100" style="background-color: var(--primary);">
        <div class="container py-5 h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
              <div class="card shadow-2-strong" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">

                  <h3 class="mb-5">Sign in</h3>
                  <form @submit.prevent="loginUser">
                    <div class="form-outline mb-4">
                      <label class="form-label" for="typeEmailX-2">User Name</label>
                      <input type="text" v-model="username" required class="form-control form-control-lg"
                        :class="{ 'is-invalid': this.error }" />
                    </div>

                    <div class="form-outline mb-4">
                      <label class="form-label" for="typePasswordX-2">Password</label>
                      <input type="password" v-model="password" required class="form-control form-control-lg"
                        :class="{ 'is-invalid': this.error }" />

                    </div>

                    <div v-if="this.error" class="alert alert-danger" role="alert">
                      {{ $t("Login Error") }}
                    </div>

                    <button class="btn btn-primary btn-lg btn-block" type="submit">Login</button>
                  </form>

                </div>
              </div>
            </div>
          </div>
        </div>
      </section>


    </div> -->

    <div>


      <main id="main">
        <router-view :search="search" />
      </main>


      <a href="#" class="scroll-top d-flex align-items-center justify-content-center active"><i
          class="bi bi-arrow-up-short"></i></a>
      <!-- ======= Footer ======= -->
      <footer id="footer" class="footer">

        <div class="footer-content position-relative">
          <div class="container">
            <div class="row">

              <div class="col-lg-4 col-md-6">
                <div class="footer-info">
                  <h3>جامعة فلسطين التقنية</h3>
                  <p>
                    كلية الهندسة والتكنلوجيا <br>
                    نادي هندسة البناء<br><br>
                    <strong>Phone:</strong> +1 5589 55488 55<br>
                    <strong>Email:</strong> info@example.com<br>
                  </p>
                  <div class="social-links d-flex mt-3">
                    <a href="#" class="d-flex align-items-center justify-content-center"><i class="bi bi-twitter"></i></a>
                    <a href="#" class="d-flex align-items-center justify-content-center"><i
                        class="bi bi-facebook"></i></a>
                    <a href="#" class="d-flex align-items-center justify-content-center"><i
                        class="bi bi-instagram"></i></a>
                    <a href="#" class="d-flex align-items-center justify-content-center"><i
                        class="bi bi-linkedin"></i></a>
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

  </div>
</template>

<script>
/* eslint-disable */
import moment from 'moment';
import axios from "axios";
import { my_api, domain_url } from "./axios-api";

// @ is an alias to /src
import SideBar from "@/components/parts/SideBar.vue";
import NavBar from "@/components/parts/NavBar.vue";
export default {
  name: "HomeView",
  components: {
    SideBar,
    NavBar,
  },
  data() {
    return {
      error: false,
      settings: {
        dark_mode: '',
        lang: '',
        primary_color: '',
        back_color: '',
      },
      auth: {
        username: '',
        password: '',
        logged_in: localStorage.getItem('access_token'),
      },
      search: NavBar.search,
      primary_color: '',
      primary_text: '',
      back_color: '',

    }
  },
  async mounted() {
    await this.get_settings();
    this.dark_mode();
    this.set_lang();
  },
  methods: {
    go_to() {
      const myDiv = document.getElementById('services'); // Replace 'myDiv' with the ID of your target div
      myDiv.scrollIntoView({ behavior: 'smooth' });
    },

    async loginUser() {
      const data = { username: this.username, password: this.password }
      try {
        const response = await axios.post(domain_url + '/backend/login/', data)
        this.auth.logged_in = response.data.access
        localStorage.setItem('access_token', this.auth.logged_in)
        localStorage.setItem('token_time', new Date())

        // redirect to dashboard or homepage after successful login
        this.error = false;
        this.$router.push('dashboard')
      } catch (error) {
        this.error = true;
        console.log(error);
      }
    },
    async logout() {
      //to remove modal background on auto vue js reload
      const elements = document.getElementsByClassName("modal-backdrop fade show");
      while (elements.length > 0) {
        elements[0].parentNode.removeChild(elements[0]);
      }////
      localStorage.setItem('access_token', '');
      this.auth.logged_in = '';
    },
    dark_mode() {
      if (this.settings.dark_mode) {
        this.primary_color = '#242526';
        this.primary_text = '#fff';
        this.back_color = '#18191a';
      } else {
        this.primary_color = this.settings.primary_color;//'#6096B4'
        this.primary_text = this.settings.primary_color;
        this.back_color = this.settings.back_color;//'#f8f9fc';
      }
    },
    get_settings() {
      return my_api.get("/backend/settings/1")
        .then((response) => (
          this.settings.dark_mode = response.data['dark_mode'],
          this.settings.primary_color = response.data['primary_color'],
          this.settings.back_color = response.data['back_color'],
          this.settings.lang = response.data['lang']
        ));
    },
    async save_settings() {
      try {
        var response = await fetch(domain_url + "/backend/settings/1/", {
          method: "PUT",
          headers: { "Content-Type": "application/json", },
          body: JSON.stringify(this.settings),
        }
        );
        swal(this.$t("Saved"), { buttons: false, icon: "success", timer: 2000, });
        await this.get_settings();
        this.dark_mode();
        this.set_lang();
        this.close_settings_modal();
      } catch (error) {
        console.error();
      }

    },
    set_lang() {
      this.$i18n.locale = this.settings.lang;
    },
    open_settings_modal() {
      $('#settings_modal').modal('toggle');
    },
    close_settings_modal() {
      $('#settings_modal').modal('hide');
    },
  },
  beforeCreate() {
    const token = localStorage.getItem('access_token')
    this.logged_in = token

    var token_time = localStorage.getItem('token_time')
    const date1 = new Date(); // Set date1 to the current date and time
    const date2 = new Date(token_time); // Set date2 to the date specified by date2String

    const diffInMs = Math.abs(date2 - date1);
    const diffInMinutes = Math.floor((diffInMs / 1000) / 60);

    if (diffInMinutes > 30) {
      localStorage.setItem('access_token', '');
      localStorage.setItem('token_time', 0)
      //this.auth.logged_in = '';
    }
  },
};
</script>
