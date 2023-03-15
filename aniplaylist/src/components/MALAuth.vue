<template>
    <a :href=msg>
    <div class='button'>
      <img src="../assets/MyAnimeList_Logo.png" class="spotify_logo">
      <p class="prompt">Log in to MyAnimeList</p>
    </div>
  </a>
</template>

<style>
.button{
  background-color: #2e51a2;
  height: 100px;
  width: 350px;
  border-radius: 20px;
  display: flex;
  flex-direction: row;
  margin: auto;
  margin-top: 20px;
}
.spotify_logo{
  height: 80px;
  margin: auto 10px;
}
.prompt {
  margin: auto ;
  color: white;
  font-size: large;
}
</style>
  
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
      const path = '/api/mal_auth';
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