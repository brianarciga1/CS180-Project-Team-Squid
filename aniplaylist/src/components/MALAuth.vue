<template>
    <div v-html="msg"></div>
</template>
  
<script>
import axios from 'axios';


export default {
  name: 'MALAuth',
  data() {
    return {
      msg: '',
      success: '',
    };
  },
  methods: {
    mal_auth() {
      const path = 'http://127.0.0.1:5173/api/mal_auth';
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
      this.$emit('malAuth')
    }

  },
  mounted() {
    this.mal_auth();
  },
};
</script>