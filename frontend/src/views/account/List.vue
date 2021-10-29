<template>
  <div class="account_list">
    <p>{{ message }}</p>
    <h3>アカウント一覧</h3>
    <v-simple-table>
      <template v-slot;default>
        <thead>
          <tr>
            <th>編集</th>
            <th>削除</th>
            <th>アカウントID</th>
            <th>アカウント名称</th>
            <th>有効開始日</th>
            <th>有効終了日</th>
            <th>作成者</th>
            <th>作成日時</th>
            <th>更新者</th>
            <th>更新日時</th>
            <th>ステータス</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="account in accounts" v-bind:key="account.id">
            <td>
              <Update v-bind:account-id="account.id"></Update>
            </td>
            <td>
              <Delete v-bind:account="account"></Delete>
            </td>
            <td>{{ account.id }}</td>
            <td>{{ account.account_name }}</td>
            <td>{{ account.start_on }}</td>
            <td>{{ account.end_on }}</td>
            <td>{{ account.created_by }}</td>
            <td>{{ account.created_at }}</td>
            <td>{{ account.updated_by }}</td>
            <td>{{ account.updated_at }}</td>
            <td>{{ account.status }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>
<script>
import Update from '@/views/account/Update.vue'
import Delete from '@/views/account/Delete.vue'

var request = {
  operation_account_id: 100
}
var url = 'http://localhost:5000/api/account/search'
const config = {
  headers: {
    'Content-Type': 'application/json'
  }
}

export default {
  name: 'List',
  data () {
    return {
      accounts: [],
      message: null
    }
  },
  mounted () {
    var self = this
    this.axios
      .post(url, request, config)
      .then(function (response) {
        console.log('List axios response %o', response.data.body)
        self.accounts = response.data.body
        self.message = response.data.status.message
      })
      .catch(err => {
        console.log('List axios error')
        console.log(err)
      })
  },
  components: {
    Update,
    Delete
  }
}
</script>
