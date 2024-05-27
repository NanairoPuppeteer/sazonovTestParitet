<script setup>
    import { ref } from 'vue';

    const img = ref(null);
    const desc = ref(null);

    const emit = defineEmits(['needUpdate']);

    async function convertBase64(file) {
        return new Promise((resolve, reject) => {
            const fileReader = new FileReader();
            fileReader.readAsDataURL(file);

            fileReader.onload = () => {
                resolve(fileReader.result);
            };

            fileReader.onerror = (error) => {
                reject(error);
            };
        });
    }

    async function send() {
        let base64image = await convertBase64(img.value.files[0]);
        let requestBody = {
            image: base64image,
            description: desc.value.value
        };

        let response = await fetch('http://localhost:8000/pictures/', {
            method: 'POST',
            headers: {
                "Accept": 'application/json',
                "Content-Type": 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        if (response.ok) {
            emit('needUpdate');
        }
    }
</script>

<template>
    <div class="form">
        <div class="form-item long">
            <label>Картинка</label><br />
            <input type="file" id="img" ref="img" />
        </div>
        <div class="form-item long">
            <label>Описание</label><br />
            <textarea id="desc" ref="desc"></textarea>
        </div>
        <div class="form-item short">
            <button @click="send">Отправить</button>
        </div>
    </div>
</template>

<style>
    .form {
        display: flex;
        justify-content: center;
        flex-direction: column;
        margin: 10px;
        padding: 10px;
        border: gray solid 1px;
        border-radius: 10px;
    }

    .form-item {
        margin: 10px;
        padding: 10px;
        width: 100%;
    }

    @media (min-width: 1024px) {
        .form {
            flex-direction: row;
        }

        .form-item.long {
            width: 45%;
        }

        .form-item.short {
            width: 10%;
        }
    }
</style>