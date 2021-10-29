<template>
  <v-dialog v-model="dialog" width="500">
    <v-btn
      fab
      x-small
      class="mx-2"
      slot="activator"
      color="red lighten-2"
      dark
      @click="dialog = true"
    >
      <v-icon dark>
        mdi-delete
      </v-icon>
    </v-btn>

    <v-card>
      <v-card-title class="headline grey lighten-2" primary-title>
        アカウント削除
      </v-card-title>
      <v-card-text>
        アカウント {{ account.account_name }} を削除します。
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions
        >
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="dialog = false">
          キャンセル
        </v-btn>
        <v-btn color="primary" text @click="dialog = false">
          削除
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: 'Delete',
  props: {
    account: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      dialog: false
    }
  }
}
</script>
