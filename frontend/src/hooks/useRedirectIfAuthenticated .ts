import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { isAuthenticated } from '../lib/auth'
import { ROUTES } from '../constants/urls'

export const useRedirectIfAuthenticated = () => {
    const navigate = useNavigate()

    useEffect(() => {
        if (isAuthenticated()) {
            navigate(ROUTES.CHAT)
        }
    }, [navigate])
}
