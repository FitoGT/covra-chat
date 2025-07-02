import { useState } from 'react'
import { User } from 'lucide-react'
import { useNavigate } from 'react-router-dom'
import covraIcon from '../assets/covra-icon.png'
import { isAuthenticated } from '../lib/auth'
import { ROUTES } from '../constants/urls'

const Header = () => {
  const navigate = useNavigate()
  const [menuOpen, setMenuOpen] = useState(false)
  const authenticated = isAuthenticated()

  const login = () => navigate(ROUTES.LOGIN)
  const register = () => navigate(ROUTES.REGISTER)
  const logout = () => {
    localStorage.clear()
    navigate(ROUTES.CHAT)
  }


  return (
    <header className="bg-white shadow-sm py-4 px-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <img src={covraIcon} alt="Covra Icon" className="h-8 w-8" />
          <h1 className="text-xl font-semibold text-gray-800">Cover Letter Generator</h1>
        </div>

        <div className="relative">
          <button
            onClick={() => setMenuOpen((prev) => !prev)}
            className="p-2 rounded-full hover:bg-gray-100 transition"
          >
            <User className="w-6 h-6 text-gray-700" />
          </button>

          {menuOpen && (
            <div className="absolute right-0 mt-2 w-36 bg-white border rounded shadow-lg z-10">
              {!authenticated ? (
                <>
                  <button
                    onClick={login}
                    className="w-full text-left px-4 py-2 hover:bg-gray-100"
                  >
                    Login
                  </button>
                  <button
                    onClick={register}
                    className="w-full text-left px-4 py-2 hover:bg-gray-100"
                  >
                    Register
                  </button>
                </>
                
              ) : (
                <button
                  onClick={() => logout()}
                  className="w-full text-left px-4 py-2 hover:bg-gray-100"
                >
                  Logout
                </button>
              )}
            </div>
          )}
        </div>
      </div>
    </header>
  )
}

export default Header
