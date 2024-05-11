<template>
    <div>
        <div class="background">
            <div class="shape"></div>
            <div class="shape"></div>
        </div>
        <form @submit.prevent="login">
            <h3>Sing Up Here</h3>

            <label for="email">Email</label>
            <input type="text" placeholder="Email" id="email" ref="emailInput" required>

            <label for="username">Username</label>
            <input type="text" placeholder="Username" id="username" ref="usernameInput" required>

            <label for="password">Password</label>
            <input type="password" placeholder="Password" id="password" ref="passwordInput" required>

            <button type="submit">Sing Up</button>
        </form>
    </div>
</template>

<script>
import axios from "axios";
import { userSessionStore } from "@/stores/counter";

export default {

  data() {
    return {
      emial: '',
      username: '',
      password: '',
      result: null // Define result en la sección data
    };
  },
  created(){
    this.userSession = userSessionStore();
  },
  methods: {
    login() {
      // Aquí puedes agregar la lógica para enviar la información de inicio de sesión al servidor
      const username = this.$refs.usernameInput.value;
      const password = this.$refs.passwordInput.value;
      const email = this.$refs.emailInput.value;

      console.log('Username:', username);
      console.log('Password:', password);
      console.log('Email:', email);

        const data = {
            username: username,
            password: password,
            email: email,
        };

        axios.post("http://127.0.0.1:8000/api/users/", data)
        .then((response) => {
            this.result = response.data;
            const data = response.data;
            console.log("Data: ",data);
            this.userSession.setRegistered()
            this.$router.push({ name: "Login" });
        })
        .catch((error) => {
            console.error('Error al realizar la solicitud POST:', error);
        });
    }
  }
};
</script>

<style scoped>
*,
*:before,
*:after {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

body {
    background-color: #080710;
}

.background {
    width: 100%;
    /* Ocupa toda la anchura */
    height: 520px;
    position: relative;
    /* Cambiado a relativo */
}

.background .shape {
    height: 200px;
    width: 200px;
    position: absolute;
    border-radius: 50%;
}

.shape:first-child {
    background: linear-gradient(#1845ad, #23a2f6);
    left: -80px;
    top: -80px;
}

.shape:last-child {
    background: linear-gradient(to right, #ff512f, #f09819);
    right: -30px;
    bottom: -80px;
}

form {
    height: 600px;
    width: 400px;
    background-color: rgba(255, 255, 255, 0.13);
    position: absolute;
    top: 50%;
    right: 25%;
    /* Alineado a la derecha */
    transform: translate(-0, -50%);
    /* Centrado verticalmente */
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
    padding: 50px 35px;
}

form * {
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
}

form h3 {
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
}

label {
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
}

input {
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
}

::placeholder {
    color: #e5e5e5;
}

button {
    margin-top: 50px;
    width: 100%;
    background-color: #ffffff;
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
}
</style>