export default function setLocalStorageDefaults () {
  if (localStorage.getItem('defaultUser') === null) {
    let user = {}
    user.name = ''
    user.email = ''
    localStorage.setItem('defaultUser', JSON.stringify(user))
  }
}
