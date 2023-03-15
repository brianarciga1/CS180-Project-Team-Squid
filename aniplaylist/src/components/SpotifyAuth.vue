<template>
  <a :href=msg>
    <div class='button'>
      <img src="../assets/Spotify_Icon_RGB_White.png" class="spotify_logo">
      <p class="prompt">Log in to Spotify</p>
    </div>
  </a>
</template>

<style>
.button{
  background-color: #1db854;
  height: 100px;
  width: 300px;
  border-radius: 20px;
  display: flex;
  flex-direction: row;
  margin: auto;
  margin-top: 20px;
}
.spotify_logo{
  height: 50px;
  margin: auto 10px;
}
.prompt {
  margin: auto 20px;
  color: white;
  font-size: x-large;
}
</style>
  
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