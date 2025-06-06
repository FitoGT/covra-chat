import type { paths } from './api'

export type LoginRequest = paths['/auth/login']['post']['requestBody']['content']['application/json']
export type LoginResponse = paths['/auth/login']['post']['responses']['200']['content']['application/json']
export type RegisterRequest = paths['/users/register']['post']['requestBody']['content']['application/json']
export type RegisterResponse = paths['/users/register']['post']['responses']['200']['content']['application/json']
export type GenerateCoverLetterRequest = paths['/cover-letter/generate']['post']['requestBody']['content']['application/json']
export type GenerateCoverLetterResponse = paths['/cover-letter/generate']['post']['responses']['200']['content']['application/json']
