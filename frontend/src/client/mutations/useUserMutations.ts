import { useMutation } from '@tanstack/react-query'
import { RegisterRequest, RegisterResponse } from '../../types/api-types'
import { saveTokenWithExpiry } from '../saveToken'

const registerFn = async (data: RegisterRequest): Promise<RegisterResponse> => {
    const res = await fetch('http://localhost:8000/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })

    if (!res.ok) throw new Error('Register failed')

    const json = await res.json()
    const token = json.access_token || json.token
    if (token) saveTokenWithExpiry(token)

    return json
}

export const useUserRegisterMutation = () => useMutation({ mutationFn: registerFn })
