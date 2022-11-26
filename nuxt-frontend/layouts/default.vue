<template>
  <v-app>

    <v-navigation-drawer 
      app 
      clipped
      expand-on-hover
      mini-variant 
      permanent
      fixed
      >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ title }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>

        </v-list-item>
      </v-list>

    </v-navigation-drawer>

    <v-main>
      <v-container fluid>
        <Nuxt />
      </v-container>
    </v-main>

  
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      items: [
        {
          icon: 'mdi-apps',
          title: 'Gallery',
          to: '/',
        },
        {
          icon: 'mdi-plus',
          title: 'Add a snippet',
          to: '/newSnippet',
        },
      ],
      title: 'MyCodingVault',
    }
  },
}
</script>
