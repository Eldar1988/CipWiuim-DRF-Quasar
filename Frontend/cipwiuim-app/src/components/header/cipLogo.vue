<template>
  <router-link to="/">
    <div id="logo">
      <div id="logo-img">
        <div id="logo-text">CIP<br>WIUIM</div>
        <img src="../../assets/logo-stars.png" alt="" id="logo-self">
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "cipLogo"
}
</script>

<style lang="sass">
#logo
  background: #003399
  position: relative
  width: 130px
  height: 55px
  border-radius: 4px
  margin: 3px 0

#logo-img
  position: absolute
  text-align: center
  width: 100%
  top: 1px

#logo-text
  position: absolute
  text-align: center
  color: #eabd1e
  top: 45%
  width: 100%
  transform: translateY(-50%)
  line-height: 1
  font-size: 12px

#logo-img img
  max-width: 53px

#logo-self
  max-width: 70px
  max-height: 50%
  animation-name: logo
  animation-duration: 20s
  animation-timing-function: linear
  animation-iteration-count: infinite
  animation-fill-mode: forwards

@keyframes logo
  0%
    transform: rotateZ(0)
  100%
    transform: rotateZ(360deg)


</style>
