export const saveTokenWithExpiry = (token: string) => {
    const expiry = Date.now() + 60 * 60 * 1000
    localStorage.setItem('token', token)
    localStorage.setItem('token_expiry', expiry.toString())
}
