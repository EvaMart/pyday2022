<template>
    <v-card
          class="ma-3">

          <v-card
            class="ma-2"
            dark
            max-width="400"
          >
            <pre class="ma-2 pa-2">{{ body }}</pre>
          </v-card>

          
          <v-card-title v-text="title"></v-card-title>
          <v-card-subtitle v-text="description"></v-card-subtitle>

          <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            v-for="(link, index) in source"
            :href="link"
            target="_blank"
            color="orange"
            link
            text
          >
            Source {{ index + 1 }}
          </v-btn>

          </v-card-actions>
        </v-card>

</template>
<script>
export default {
  name: 'Card',
  props: ["title", "description", "body", "source"],
}
</script>