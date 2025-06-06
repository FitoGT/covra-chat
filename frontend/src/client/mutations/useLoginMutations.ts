import { useMutation } from '@tanstack/react-query'
import { LoginRequest, LoginResponse } from '../../types/api-types'
import { saveTokenWithExpiry } from '../saveToken'

const loginFn = async (data: LoginRequest): Promise<LoginResponse> => {
    const res = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })

    if (!res.ok) throw new Error('Login failed')

    const json = await res.json()
    const token = json.access_token || json.token
    if (token) saveTokenWithExpiry(token)

    return json
}

export const useLoginMutation = () => useMutation({ mutationFn: loginFn })
