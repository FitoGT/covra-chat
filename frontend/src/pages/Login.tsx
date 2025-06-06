import { useNavigate, Link } from 'react-router-dom'
import { loginSchema } from '../lib/zodSchemas'
import { AuthForm } from '../components/AuthForm'
import { login } from '../client/api-client'

export default function Login() {
  const navigate = useNavigate()

  const handleLogin = async (data: any) => {
    try {
      await login(data.email, data.password)
      navigate('/chat')
    } catch (err) {
      alert('Invalid credentials')
    }
  }

  return (
    <div className="max-w-md mx-auto mt-20">
      <h2 className="text-2xl font-semibold mb-6">Login</h2>
      <AuthForm
        schema={loginSchema}
        onSubmit={handleLogin}
        fields={[
          { name: 'email', label: 'Email', type: 'email' },
          { name: 'password', label: 'Password', type: 'password' },
        ]}
        buttonText="Log In"
      />
      <p className="mt-4 text-sm">
        Don’t have an account? <Link to="/register" className="text-indigo-600">Register here</Link>
      </p>
    </div>
  )
}
