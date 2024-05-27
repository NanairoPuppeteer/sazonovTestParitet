<script setup>
    const props = defineProps({
        id: Number,
        image: String,
        description: String,
    });

    const emit = defineEmits(['needUpdate']);

    async function deleteItem (id) {
        let response = await fetch('http://localhost:8000/pictures/' + id, {
            method: 'DELETE',
            headers: {
                "Accept": 'application/json'
            }
        });

        if (response.ok) {
            emit('needUpdate');
        }
    }
</script>

<template>
    <div class="picture-item">
        <div class="picture-item-img">
            <img :src="image" />
        </div>
        <div class="picture-item-description">
            {{ description }}
        </div>
        <div class="picture-item-delete">
            <button @click="deleteItem(id)">Удалить</button>
        </div>
    </div>
</template>

<style>
.picture-item {
    display: flex;
    flex-direction: column;
    padding: 10px;
    margin: 10px;
    border: gray solid 1px;
    border-radius: 10px;
}

.picture-item-img {
    width: 100%;
}

.picture-item-img img {
    display: block;
    margin: auto;
    max-width: 100%;
    max-height: 150px;
}

.picture-item-description {
    width: 100%;
    text-align: center;
    padding: 10px;
}

.picture-item-delete {
    width: 100%;
    text-align: center;
    padding: 10px;
}

@media (min-width: 1024px) {
    .picture-item {
        flex-direction: row;
    }
    .picture-item-img {
        width: 45%;
    }

    .picture-item-description {
        text-align: left;
        width: 45%;
    }

    .picture-item-delete {
        text-align: left;
        width: 10%;
    }
}

</style>