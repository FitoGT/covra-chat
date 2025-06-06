import { useNavigate, Link } from 'react-router-dom'
import { registerSchema } from '../lib/zodSchemas'
import { AuthForm } from '../components/AuthForm'
import { register } from '../client/api-client'

export default function Register() {
  const navigate = useNavigate()

  const handleRegister = async (data: any) => {
    try {
      await register(data.name, data.email, data.password, data.confirmPassword)
      navigate('/login')
    } catch (err) {
      alert('Registration failed')
    }
  }

  return (
    <div className="max-w-md mx-auto mt-20">
      <h2 className="text-2xl font-semibold mb-6">Register</h2>
      <AuthForm
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
        Already have an account? <Link to="/login" className="text-indigo-600">Login here</Link>
      </p>
    </div>
  )
}
