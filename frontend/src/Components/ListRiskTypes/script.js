import Vue from 'vue'
import axios from 'axios'

import buildForm from '../buildForm/index'

export default {
  data () {
    return {
      riskTypes: [],
      errors: []
    }
  },
  components: {
    buildForm
  },

  created () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/snippets/?format=json',
      responseType: 'json'
    })
      .then((response) => {
        this.riskTypes = response.data
        console.log(response)
      })
      .catch((e) => {
        this.errors.push(e)
      })
  }
};

