<template>
    <v-card
        class="ma-3 pt-1">
        <v-card
            class="mt-2 ml-2 mr-2"
            color="#2d2d2d"
            dark>
            <vue-code-highlight 
            language="python"
            class="mr-0 ml-0 mt-2">
                <pre>{{body}}</pre>
            </vue-code-highlight>
        </v-card>
          
          <v-card-title 
            class="text-h6 mt-0 mb-2 pt-1 card-title"
            v-text="title">
          </v-card-title>
          
          <v-card-subtitle 
            class="mb-0 pb-0 card-description"
            v-text="description"> </v-card-subtitle>

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
<style scoped>
.v-card  >>> .card-title {
    word-break: normal;
    font-size: 1.2rem !important; 
    font-weight: 500 !important;
    line-height: 1.3 !important;
}

.v-card >>> .card-description {
    white-space: pre-wrap
}

</style>
<script>
import { component as VueCodeHighlight } from 'vue-code-highlight';
import "vue-code-highlight/themes/prism-tomorrow.css";
import 'prism-es6/components/prism-python';

export default {
  name: 'Card',
  props: ["title", "description", "body", "source"],
  components: {
    VueCodeHighlight
  }
}
</script>