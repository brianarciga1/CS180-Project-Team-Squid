<!--THIS IS FOR THE HOME PAGE!!!!-->
<template>
  <div class="Home">
    <strong class="font1"> HOW___TO___USE</strong>
    <p class="font2">1.) Click authenticate</p>
    <p class="font2">2.) Login to Spotify</p>
    <p class="font2">3.) Login to My Anime List</p>
    <p class="font2">4.) Fill in the details for your new playlist</p>
    <p class="font2">And you're done!</p>
    <div class="spacer"></div>
    <strong class="font1"> OUR___MOTIVE</strong>
    <p class="font2">The purpose of our project is to provide a convenient way for people to listen to their favorite anime music!<br>This project will eliminate the hassle of googling or tracking down the song titles.</p>
    <div class="spacer"></div>
    <div class="center">
      <img src="@/assets/images/Team_Squid.png" alt="centered image" style="max-width: 20%;">
    </div>
    <strong class="font3"> FRONT-END___TEAM</strong>
    <p class="font4">Brian Arciga, Luis Angulo, Randy Zuniga</p>
    <div class="spacer"></div>
    <strong class="font3"> BACK-END___TEAM</strong>
    <p class="font4">William Feng, Edward Segura, Jordan Chan</p>
    <div class="spacer"></div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  props: {
    msg: String
  }
}
</script>

<style scoped>

@font-face {
  font-family: "Naruto";
  src: url(@/assets/fonts/NinjaNaruto-YOn4.ttf);
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
  margin-bottom: 100px;
  background-color: black;
}

.spacer {
  height: 50px; /* adjust as needed */
}

.font1 {
  font-family: "Naruto", sans-serif;
  font-size: 70px;
  text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
  border: 10px solid rgba(199, 3, 166, 0.322);
  border-radius:10px;
  background-color: rgba(199, 3, 166, 0.452);
}
.font2 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
  font-weight: bold;
  border: 10px solid rgba(0, 0, 0, 0.393);
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
  background-color: rgba(135, 28, 117, 0.233);
}
.font3 {
  font-family: "Naruto", sans-serif;
  font-size: 40px;
  text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
}
.font4 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
  font-weight: bold;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
}
</style>





