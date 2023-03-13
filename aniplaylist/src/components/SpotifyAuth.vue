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
      complete: false,
    };
  },
  methods: {
    sp_auth() {
      const path = '/api/sp_auth';
      const queryString = window.location.search
      if(queryString == ''){
        axios.get(path)
        .then((res) => {
          this.msg = res.data;
          if(this.msg == 'auth complete'){
            this.emitToParent()
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      }
      else{
        axios.get(path+queryString)
        .then((res) => {
          this.emitToParent()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      }
    },
    emitToParent(){
      this.$emit('spotAuth')
    }
  },
  mounted() {
    this.sp_auth();
  },
};
</script>