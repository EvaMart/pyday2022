<template>
    
</template>
<script>
export default {
  data: () => ({
    snackbar: false,
  }),
    props: {
        text: {
        type: String,
        default: 'Default text',
        },
    },
  methods: {
    showSnackbar(text) {
      this.text = text;
      this.snackbar = true;
    },
  },
};