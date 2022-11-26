<template>
    <v-container fluid>
    <v-row dense>
      <v-col
        v-for="card in cards"
        :key="card.title"
        lg="3"
        md="6"
        sm="12"
        xs="12"
        >
        <CardHighlighted
          :title="card.title"
          :description="card.description"
          :body="card.body"
          :source="card.source" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import CardHighlighted from '../components/CardHighlighted.vue';
import { mapGetters } from 'vuex';

export default {
    name: "index",
    computed: {
        ...mapGetters({
            cards : 'getCards',
          })
        },
    created() {
        this.$store.dispatch('requestCards');
    },
    components: { CardHighlighted}
}
</script>
