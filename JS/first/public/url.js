const URLSITE = "http://localhost:8000/api/auth/account/activate/hsakdjaklndasdaskdnas"

const url = new URL(URLSITE)
console.log(url.pathname.split("/").slice(-1)[0] )