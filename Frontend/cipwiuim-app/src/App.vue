<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
import {Notify} from "quasar"
import setLocalStorageDefaults from "src/utils/setLocalStorageDefaults"
export default {
  name: 'App',
  created() {
    Notify.setDefaults({
      position: 'top',
      timeout: 5000,
      textColor: 'white',
      actions: [{ icon: 'close', color: 'white' }]
    })
    setLocalStorageDefaults()
  }
}
</script>
