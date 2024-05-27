<script setup>
  import { ref } from 'vue';
  import PicturesList from './components/PicturesList.vue';
  import PictureForm from './components/PictureForm.vue';

  const pictures = ref(null);
  const isLoading = ref(true);

  async function fetchPictures() {
    isLoading.value = true;
    let response = await fetch('http://localhost:8000/pictures/', {
      method: 'GET',
      headers: {
        "Accept": 'application/json'
      }
    });
    let result = await response.json();
    pictures.value = result;
    isLoading.value = false;
  }

  fetchPictures();
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <div class="title">
        <h1 class="green">Список картинок</h1>
      </div>
    </div>
  </header>

  <main>
    <PictureForm @needUpdate="fetchPictures()" />
    <PicturesList @needUpdate="fetchPictures()" v-if="!isLoading" :picturesItems="pictures" />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
  margin: 2rem;
  display: flex;
  place-items: center;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

@media (min-width: 1024px) {

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
    width: 100%;
  }

  header .wrapper div {
    margin: auto;
  }
}
</style>
