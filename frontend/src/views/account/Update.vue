<template>
  <v-dialog v-model="dialog" width="800">
    <v-btn
      fab
      x-small
      class="mx-2"
      slot="activator"
      color="cyan"
      dark
      @click="
        getAccount();
        dialog = true;
      "
    >
      <v-icon dark>
        mdi-pencil
      </v-icon>
    </v-btn>

    <v-card>
      <v-card-title class="headline grey lighten-2" primary-title>
        アカウント更新
      </v-card-title>

      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field
                label="アカウントid"
                disabled
                required
                v-model="account.id"
              ></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field
                label="アカウント名称"
                required
                v-model="account.account_name"
              ></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-menu max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="account.start_on"
                    :value="account.start_on"
                    label="有効開始日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="account.start_on"></v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs12>
              <v-menu max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="account.end_on"
                    :value="account.end_on"
                    label="有効終了日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="account.end_on"></v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs12>
              <v-text-field
                label="作成者"
                required
                v-model="operation_account_id"
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          text
          @click="
            submit();
            dialog = false;
          "
        >
          更新
        </v-btn>
        <v-btn color="primary" text @click="dialog = false">
          キャンセル
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
var url = 'http://localhost:5000/api/account/'
const config = {
  headers: {
    'Content-Type': 'application/json'
  }
}

function applyDateFormat (datestring) {
  if (datestring.search(/^\d{4}[-/]\d{2}[-/]\d{2} \d{2}:\d{2}:\d{2}$/) === 0) {
    return datestring
  } else if (datestring.search(/^\d{4}[-/]\d{2}[-/]\d{2}$/) === 0) {
    return datestring.concat(' 00:00:00')
  }
}

function setAccount (account) {
  var a = {
    id: account.id,
    account_name: account.account_name,
    start_on: applyDateFormat(account.start_on),
    end_on: applyDateFormat(account.end_on)
  }
  return a
}

export default {
  name: 'Update',
  props: {
    accountId: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      dialog: false,
      account: {
        id: '',
        account_name: '',
        start_on: '',
        end_on: ''
      },
      operation_account_id: 50
    }
  },
  computed: {
    form () {
      return {
        id: this.account.id,
        account_name: this.account.account_name,
        start_on: applyDateFormat(this.account.start_on),
        end_on: applyDateFormat(this.account.end_on),
        operation_account_id: parseInt(this.operation_account_id)
      }
    }
  },
  methods: {
    getAccount () {
      var request = {
        id: this.accountId,
        operation_account_id: parseInt(this.operation_account_id)
      }
      console.log('getAccount was called')
      const self = this
      this.axios
        .post(url + 'lock', request, config)
        .then(function (response) {
          console.log('Get axios response')
          console.log(response)
          self.account = setAccount(response.data.body)
          self.meesage = response.status.message
        })
        .catch(err => {
          console.log('Get axios error')
          console.log(err)
        })
    },
    validate () {
      this.$refs.form.validate()
    },
    submit () {
      console.log(this.form)
      this.axios
        .post(url + 'update_for_lock', this.form, config)
        .then(function (response) {
          console.log('Update axios response')
          console.log(response)
          document.location = 'http://localhost:8080/account'
        })
        .catch(err => {
          console.log('Update axios error')
          console.log(err)
        })
    }
  }
}
</script>
