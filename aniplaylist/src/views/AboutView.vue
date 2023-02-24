<template>
  <SpotifyAuth />
</template>

<script>
import MALAuth from '../components/MALAuth.vue';
import SpotifyAuth from '../components/SpotifyAuth.vue';

export default {
    name: "Search",
    props: {
        msg: String
    },
    components: { SpotifyAuth, MALAuth }
}
</script>

<style scoped>

</style>