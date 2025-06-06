export const isAuthenticated = () => {
    const token = localStorage.getItem('token')
    const expiry = localStorage.getItem('token_expiry')

    if (!token || !expiry) return false

    return Date.now() < Number(expiry)
}