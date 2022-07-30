import { createStore } from 'vuex';
import { auth } from './auth.module';

let storedLocale = localStorage.getItem('locale');

let initialState = {
  locale: storedLocale ? storedLocale : 'EN'
}

export default createStore({
  state() {
    return initialState;
  },
  mutations: {
    setLocale(state, newLocale) {
      state.locale = newLocale;
    }
  },
  actions: {
    setLocale(context, newLocale) {
      context.commit('setLocale', newLocale)
      localStorage.setItem('locale', newLocale);
    }
  },
  modules: {
    auth
  }
})
