import { useNavigate, Link } from 'react-router-dom'
import { loginSchema } from '../lib/zodSchemas'
import { AuthForm } from '../components/AuthForm'
import type { LoginRequest } from '../types/api-types'
import { ROUTES } from '../constants/urls'
import { useRedirectIfAuthenticated } from '../hooks/useRedirectIfAuthenticated'
import { useLoginMutation } from '../client/mutations/useLoginMutations'


export default function Login() {
  useRedirectIfAuthenticated()
  const navigate = useNavigate()
  const { mutateAsync } = useLoginMutation()


  const handleLogin = async (data: LoginRequest) => {
    try {
      await mutateAsync(data)
      navigate(ROUTES.CHAT)
    } catch (err) {
      console.error(err)
      alert('Invalid credentials')
    }
  }

  return (
    <div className="max-w-md mx-auto mt-20">
      <h2 className="text-2xl font-semibold mb-6">Login</h2>
      <AuthForm<LoginRequest>
        schema={loginSchema}
        onSubmit={handleLogin}
        fields={[
          { name: 'email', label: 'Email', type: 'email' },
          { name: 'password', label: 'Password', type: 'password' },
        ]}
        buttonText="Log In"
      />
      <p className="mt-4 text-sm">
        Don’t have an account?{' '}
        <Link to="/register" className="text-indigo-600">Register here</Link>
      </p>
    </div>
  )
}
