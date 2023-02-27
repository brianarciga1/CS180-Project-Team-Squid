<template>
  <SpotifyAuth @spot-auth="spot"/>
</template>

<script>
import SpotifyAuth from '../components/SpotifyAuth.vue';

export default {
    name: "Search",
    data(){
      return {
        spotSuccess: false,
      }
    },
    components: { SpotifyAuth},
    methods: {
      spot(){
        this.spotSuccess = true;
        this.checkAuth()
      },
      checkAuth(){
        if(this.spotSuccess == true){
          this.$router.push('/malauth');
        }
      }
      
    },
    beforeUpdate(){
      this.checkAuth();
    }
}
</script>