
<template>
  <div class="about">
    <p>{{ message }}</p>
    <h1>アカウント</h1>
    <v-form ref="form">
      <v-simple-table>
        <thead></thead>
        <tbody>
          <tr>
            <th>アカウント名称</th>
            <td>
              <v-text-field
                v-model="account_name"
                :counter="64"
                :rules="nameRules"
                :value="account_name"
                label="アカウント名称"
                required
              ></v-text-field>
            </td>
          </tr>
          <tr>
            <th>有効開始日</th>
            <td>
              <v-menu v-model="menu" max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="start_on"
                    :value="start_on"
                    label="有効開始日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="start_on"></v-date-picker>
              </v-menu>
            </td>
          </tr>
          <tr>
            <th>有効終了日</th>
            <td>
              <v-menu v-model="menu" max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="end_on"
                    :value="end_on"
                    label="有効終了日"
                    readonly
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="end_on"></v-date-picker>
              </v-menu>
            </td>
          </tr>
          <tr>
            <th>作成者</th>
            <td>
              <v-text-field
                v-model="created_by"
                :value="created_by"
                :counter="10"
                :rules="nameRules"
                label="作成者"
                required
              ></v-text-field>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
      <v-btn class="mr-4" @click="submit">保存</v-btn>
      <v-btn @click="reset">リセット</v-btn>
    </v-form>
  </div>
</template>
<script>

var contentType = 'application/json'
var url = 'http://localhost:5000/api/account/create'
const config = {
  headers: {
    'Content-Type': contentType
  }
}

export default {
  name: 'account_create',
  data: function () {
    return {
      account_name: '',
      start_on: '',
      end_on: '',
      created_by: '',
      message: '出力メッセージ'
    }
  },
  computed: {
    form () {
      return {
        account_name: this.account_name,
        start_on: this.start_on.concat(' 00:00:00'),
        end_on: this.end_on.concat(' 00:00:00'),
        operation_account_id: parseInt(this.created_by)
      }
    }
  },
  methods: {
    validate () {
      this.$refs.form.validate()
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
    submit () {
      console.log(this.form)
      this.axios
        .post(url, this.form, config)
        .then(function (response) {
          console.log('Create axios response')
          console.log(response)
          document.location = 'http://localhost:8080/account'
        })
        .catch(err => {
          console.log('Create axios error')
          console.log(err)
        })
    },
    clear () {
      this.$v.$reset()
      this.account_name = ''
      this.start_on = ''
      this.end_on = ''
      this.created_by = ''
    }

  }
}
</script>
