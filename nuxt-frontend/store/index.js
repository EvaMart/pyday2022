import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

// almacenamiento central de vuex
export const state = () => ({
    cards : [],
});


// Accesores o getters
// accesores para coger datos desde los componentes
// Normalmente se llaman desde las popriedades computed de los componentes

export const getters = {
    getCards(state){
        return state.cards
    }
   
}

// Acciones - Metodos publicos
// Estas funciones sirven para llamar a las mutaciones desde los componentes
// A diferencia de las mutaciones, pueden ser asincronas (llamadas APIs)
// Pueden tener algo de business logic y pueden llamar a varias mutaciones
export const actions = {
    /**
     * Esta función se ejecuta al inicializarse la app
     * @param {*} vuexContext commit, dispatch, state
     * @param {*} context es el mismo de asyncData y aqui tenemos acceso a toda la app: app. $axios, env, ...
     */
    async nuxtServerInit({ dispatch }, context) {
      
      },

    async requestCards({ commit }) {
        const response = await this.$axios.get('http://localhost:3500/snippet');
        commit('SET_CARDS', response.data);
    },
    
}
// Mutadores
// El 'unico fin de los mutadores es mutar o modificar state o almacenamiento
// No deben ser llamadas desde los componentes

export const mutations = {
    SET_CARDS(state, cards) {
        state.cards = cards;
    }
}