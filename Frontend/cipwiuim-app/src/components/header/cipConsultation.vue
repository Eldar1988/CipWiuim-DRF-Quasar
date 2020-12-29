<template>
<div :class="hideOnMobile ? `hide-on-mobile` : `hide-on-desktop q-pa-md`">
  <q-btn
    dense
    :outline="outline"
    :color="color"
    label="Консультация"
    :class="hideOnMobile ? `hide-on-mobile q-mr-lg q-px-md` : `hide-on-desktop q-mr-lg q-px-md full-width q-py-sm`"
    @click="dialog = true"
  />

  <q-dialog v-model="dialog" >
    <q-card style="width: 400px; max-width: 90vw;">
      <q-toolbar class="bg-primary text-white">
        <q-toolbar-title><span class="text-weight-bold q-ml-sm">Консультация</span></q-toolbar-title>
        <q-btn flat round dense icon="mdi-close" v-close-popup />
      </q-toolbar>
      <q-card-section>
        <p>Оставьте свои контактные данные.<br>Мы свяжемся с вами в ближайшее время.</p>
        <q-form>
          <q-input filled v-model="name" label="Ваше имя*" class="q-mt-sm" />
          <q-input type="number" filled v-model="phone" label="Номер телефона*" class="q-mt-sm" />
          <q-btn
            label="Отправить"
            class="q-mt-md q-py-sm full-width"
            color="primary"
            icon-right="mdi-send-check"
          />
        </q-form>
      </q-card-section>
    </q-card>
  </q-dialog>
</div>
</template>

<script>
export default {
name: "cipConsultation",
  props: {
    color: {
      type: String,
      default: 'white'
    },
    outline: {
      type: Boolean,
      default: true
    },
    hideOnMobile: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      dialog: false,
      name: '',
      phone: ''
    }
  },
}
</script>

<style scoped>

</style>
