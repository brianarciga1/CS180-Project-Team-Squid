<template>
  <SpotifyAuth @spot-auth="spot"/>
</template>

<script>
import MALAuth from '../components/MALAuth.vue';
import SpotifyAuth from '../components/SpotifyAuth.vue';

export default {
    name: "Search",
    data(){
      return {
        spotSuccess: false,
        MALSuccess: false
      }
    },
    props: {
        msg: String
    },
    components: { SpotifyAuth, MALAuth },
    methods: {
      spot(){
        this.spotSuccess = true;
        this.checkAuth()
      },
      checkAuth(){
        if(this.spotSuccess == true){
          this.$router.push('/options');
        }
      }
      
    },
    beforeUpdate(){
      this.checkAuth();
    }
}
</script>

<style scoped>

</style>