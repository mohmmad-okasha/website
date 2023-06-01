import axios from 'axios';
var currentURL = window.location.protocol + "//" + window.location.hostname + ":8000" + window.location.pathname;

const domain_url = currentURL;

const my_api = axios.create({
    baseURL: domain_url,
    timeout: 1000
});



export { my_api, domain_url }