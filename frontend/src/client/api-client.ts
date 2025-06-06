const API_BASE = 'http://localhost:8000'

/**
 * Generate a cover letter based on CV and job description
 * @param cv The user's CV
 * @param jobDescription The job description
 * @returns The generated cover letter
 */
export const generateCoverLetter = async (cv: string, jobDescription: string): Promise<string> => {
  try {
    const response = await fetch(`${API_BASE}/cover-letter/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({
        cv,
        job_description: jobDescription,
      }),
    })

    if (!response.ok) {
      throw new Error('Failed to generate cover letter')
    }

    const data = await response.json()
    return data.cover_letter
  } catch (error) {
    console.error('Error generating cover letter:', error)
    throw error
  }
}

/**
 * Register a new user
 * @param name
 * @param email
 * @param password
 * @returns JWT token or success status
 */
export const register = async (name: string, lastname: string, email: string, password: string): Promise<void> => {
  const response = await fetch(`${API_BASE}/user/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name, email, lastname, password }),
  })

  if (!response.ok) {
    throw new Error('Failed to register')
  }
}

/**
 * Login an existing user
 * @param email
 * @param password
 * @returns JWT token string
 */
export const login = async (email: string, password: string): Promise<string> => {
  const response = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  })

  if (!response.ok) {
    throw new Error('Failed to login')
  }

  const data = await response.json()
  const token = data.access_token || data.token
  if (!token) {
    throw new Error('Token not found in response')
  }

  localStorage.setItem('token', token)
  return token
}
