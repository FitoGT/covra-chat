import { useNavigate, Link } from 'react-router-dom'
import { registerSchema } from '../lib/zodSchemas'
import { AuthForm } from '../components/AuthForm'
import { register } from '../client/api-client'
import type { RegisterRequest } from '../types/api-types'

export default function Register() {
  const navigate = useNavigate()

  const handleRegister = async (data: RegisterRequest) => {
    try {
      await register(data)
      navigate('/chat')
    } catch (err) {
      console.error(err)
      alert('Registration failed')
    }
  }

  return (
    <div className="max-w-md mx-auto mt-20">
      <h2 className="text-2xl font-semibold mb-6">Register</h2>
      <AuthForm<RegisterRequest>
        schema={registerSchema}
        onSubmit={handleRegister}
        fields={[
          { name: 'name', label: 'Name' },
          { name: 'email', label: 'Email', type: 'email' },
          { name: 'password', label: 'Password', type: 'password' },
        ]}
        buttonText="Register"
      />
      <p className="mt-4 text-sm">
        Already have an account?{' '}
        <Link to="/login" className="text-indigo-600">Login here</Link>
      </p>
    </div>
  )
}
