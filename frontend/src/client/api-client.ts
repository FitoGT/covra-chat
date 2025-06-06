import {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  RegisterResponse,
  GenerateCoverLetterRequest,
  GenerateCoverLetterResponse
} from '../types/api-types'

export const login = async (data: LoginRequest): Promise<LoginResponse> => {
  const res = await fetch('http://localhost:8000/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })

  if (!res.ok) throw new Error('Login failed')

  const json = await res.json()
  const token = json.access_token || json.token
  if (token) localStorage.setItem('token', token)

  return json
}

export const register = async (data: RegisterRequest): Promise<RegisterResponse> => {
  const res = await fetch('http://localhost:8000/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })

  if (!res.ok) throw new Error('Register failed')

  return res.json()
}

/**
 * Generate a cover letter based on CV and job description
 * @param cv The user's CV
 * @param jobDescription The job description
 * @returns The generated cover letter
 */
export const generateCoverLetter = async (
  data: GenerateCoverLetterRequest
): Promise<GenerateCoverLetterResponse> => {

  const response = await fetch('http://localhost:8000/cover-letter/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error('Failed to generate cover letter')
  }

  return response.json()
}
