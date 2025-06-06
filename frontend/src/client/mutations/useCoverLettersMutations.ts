import { useMutation } from '@tanstack/react-query'
import {
    GenerateCoverLetterRequest,
    GenerateCoverLetterResponse
} from '../../types/api-types'

const generateCoverLetterFn = async (
    data: GenerateCoverLetterRequest
): Promise<GenerateCoverLetterResponse> => {
    const res = await fetch('http://localhost:8000/cover-letter/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })

    if (!res.ok) throw new Error('Failed to generate cover letter')

    return res.json()
}

export const useGenerateCoverLetterMutation = () => useMutation({ mutationFn: generateCoverLetterFn })
