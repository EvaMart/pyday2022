<template>
  <v-container>
    <v-row justify="center">
      <h5 class="text-h5 mt-3">Add a new snippet</h5>
    </v-row>
    <v-row
      justify="center">
      <v-col
       md="6"
       sm="8"
       xs="10">
       
       <v-form
        ref="form"
        method="POST"
        enctype="text/plain"
        @submit.prevent="submit"
        v-model="valid"
        lazy-validation
      >
          <v-text-field
            v-model="title"
            label="Title"
            required
          ></v-text-field>

          <v-textarea
            label="Description"
            auto-grow
            required
            rows="4"
            v-model="description"
          ></v-textarea>


          <v-combobox
            v-model="source"
            hint="Must be URLs"
            label="Add your sources"
            multiple
            small-chips
            append-icon=""
          > 
          </v-combobox>

          <v-combobox
            v-model="tags"
            :items="tag_labels"
            hint=""
            label="Add your tags"
            multiple
            small-chips
          > 
          
          </v-combobox>

          <v-textarea
            label="Body/Code"
            auto-grow
            required
            rows="6"
            v-model="body"
          ></v-textarea>

          <v-select
            v-model="select"
            :items="types"
            label="Type"
            required
          ></v-select>

          <v-btn
            color="success"
            class="mr-4"
            @click="submit"
          >
            Submit
          </v-btn>

          <v-btn
            color="error"
            class="mr-4"
            @click="reset"
          >
            Reset
          </v-btn>

        </v-form>

      </v-col>


      <v-snackbar
        v-model="snackbar"
      >
      {{ snackbar_text }}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="pink"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
    </v-row>
   
</v-container>
</template>
<script>
import SnackBar from '../components/SnackBar.vue';

export default {
    data: () => ({
        valid: false,
        title: "",
        description: "",
        body: "",
        source: [],
        tags: [],
        select: null,
        types: [
            "Code",
            "Notes",
            "Bibliography",
        ],
        tag_labels: [
            "Python",
            "Javascript",
            "Java",
            "data sctructures",
            "algorithms",
            "web development"
        ],
        snackbar: false,
        snackbar_text: "",
    }),
    methods: {
        async submit() {
            let BASE_URL = "http://localhost:3500/snippet";
            let data = {
                title: this.title,
                description: this.description,
                body: this.body,
                source: this.source,
                tags: this.tags,
                type: this.select
            };
            let result = await this.$axios.post(BASE_URL, data, {
                headers: {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json"
                }
            });
            console.log(result);
            if(result["status"] == 201) {
                this.snackbar_text = "Snippet created successfully";
                this.snackbar = true;
            } else {
                this.snackbar_text = "Snippet creation failed";
                this.snackbar = true;
            }
            this.reset();
            return result.data.data;
        },
        reset() {
            this.$refs.form.reset();
        },
    },
    components: { SnackBar }
}
</script>
