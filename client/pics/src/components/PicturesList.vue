<script setup>
    import PictureItem from './PictureItem.vue';

    const props = defineProps({
        picturesItems: Array
    });

    const emit = defineEmits(['needUpdate']);
</script>

<template>
    <div v-for="item in picturesItems">
        <PictureItem @needUpdate="emit('needUpdate')" v-bind="item" :key="item.id" />
    </div>
</template>