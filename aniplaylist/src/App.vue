<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'

</script>

<template>
  <header>
    

    <div class="wrapper">
      <HelloWorld/>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}


/*Lets menu be side by side and changes border width and color*/
nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid white;
}

nav a:first-of-type {
  border: 1;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  /*Space between logo and Title and menu*/
  .logo {
    margin: 0 2rem 0 0;
  }

  /*wrap menu around text*/
  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  /*Aligns menu with title and logo*/
  nav {
    text-align: center;
    margin-left: -1rem;
    font-size: 1rem;

    padding: -0rem 0;
    margin-top: 0rem;
  }
}

#app {
  font-family: Arial, Helvetica, sans-serif;

  
}

</style>
