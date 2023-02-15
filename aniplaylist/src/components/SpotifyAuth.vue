<template>
    <div v-html="msg"></div>
</template>
  
<script>
import axios from 'axios';


export default {
  name: 'SpotifyAuth',
  data() {
    return {
      msg: '',
      success: '',
    };
  },
  methods: {
    sp_auth() {
      const path = 'http://127.0.0.1:5000/sp_auth';
      const queryString = window.location.search
      if(queryString == ''){
        axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      }
      else{
        axios.get(path+queryString)
        .then((res) => {
          this.success = res.data;
          console.log(this.success)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      }
      
    },

  },
  mounted() {
    this.sp_auth();
  },
};
</script>